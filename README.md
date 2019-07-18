
# Demo-101
# Automate  creating Inatnces

 * Creating EC2 using the code above.
 * creating EC2 through CLI:

  ```
   aws ec2 run-instances --image-id <ami-xxxxxxx> --count 1 --instance-type t2.nano --key-name <ur_key> --security-group-ids <sg-xxxx> --subnet-id <subnet-xxxx>
  ```
  To create your aws key-name throuh CLI

  ```
   https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-keypairs.html

  ```
# Demo-102
AWS Lmabda and dyamodb
