#How to run
1. Clone the repo
'git clone https://github.com/dixi3/hackitall-prob.git'
2. Start the services
'docker-compose up -d'
3. Run the vending machine program
'docker exec -it $(docker ps | grep local | awk '{print $1}')  python3 ./hackitall.py'

Also you should be on an *nix system for it to work