use anyhow::{Error, Result};
use rclrs::*;

fn main() -> Result<(), Error> {
    let context = Context::default_from_env()?;
    let mut executor = context.create_basic_executor();

    let node = executor.create_node("text_to_cmd_vel")?;

    let worker = node.create_worker::<usize>(0);

    let publisher = node.create_publisher::<geometry_msgs::msg::Twist>("cmd_vel")?;

    let _subscription = worker.create_subscription::<std_msgs::msg::String, _>(
        "text",
        move |msg: std_msgs::msg::String| {
            let command = msg.data;

            println!("Command received: '{}'", command);

            let mut message = geometry_msgs::msg::Twist::default();

            if command.contains("command1") {
                message.linear.x = 2.0;
            } else if command.contains("command2") {
                message.linear.x = 1.0;
            } else {
                message.linear.x = 0.0;
            }
            
            publisher.publish(&message).unwrap();
        },
    )?;

    println!("Waiting for messages...");
    executor.spin(SpinOptions::default()).first_error()?;
    Ok(())
}
