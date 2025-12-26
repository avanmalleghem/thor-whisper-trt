use anyhow::{Error, Result};
use rclrs::*;
use std::sync::Arc;

fn main() -> Result<(), Error> {
    let context = Context::default_from_env()?;
    let mut executor = context.create_basic_executor();

    let node = executor.create_node("text_to_cmd_vel")?;

    let worker = node.create_worker::<usize>(0);

    let publisher = node.create_publisher::<geometry_msgs::msg::Twist>("cmd_vel")?;

    let commands: ReadOnlyParameter<Arc<[Arc<str>]>> = node.declare_parameter("commands").default_string_array(["command1", "command2"]).read_only()?;
    let linear: ReadOnlyParameter<Arc<[f64]>> = node.declare_parameter("linear").default_from_iter([2.0, 1.0]).read_only()?;
    let angular: ReadOnlyParameter<Arc<[f64]>> = node.declare_parameter("angular").default_from_iter([0.0, 0.5]).read_only()?;

    let _subscription = worker.create_subscription::<std_msgs::msg::String, _>(
        "text",
        move |msg: std_msgs::msg::String| {
            let command = msg.data;

            log!(node.logger(), "Command received: '{command}'");

            let mut message = geometry_msgs::msg::Twist::default();
            
            for cmd in commands.get().iter().enumerate() {
                if command.contains(cmd.1.as_ref()) {
                    message.linear.x = linear.get()[cmd.0];
                    message.angular.z = angular.get()[cmd.0];
                    break;
                }
            }
            
            publisher.publish(&message).unwrap();
        },
    )?;

    executor.spin(SpinOptions::default()).first_error()?;
    Ok(())
}
