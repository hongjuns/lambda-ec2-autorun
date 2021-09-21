# AWS EC2 인스턴스 자동 시작/중지

구현하고자 하는 프로세스는 아래와 같다.

1. 특정 시간에 Lambda 호출 (CloudWatch events)
2. Lambda가 호출되는 시점에 ec2 인스턴스에 등록된 모든 태그를 조회 후 
   특정 태그값이 있는 인스턴스만 인스턴스 상태를 확인하여 **start_instances** 또는 **stop_instances** 함수를 호출