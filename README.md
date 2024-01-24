## PreRequisites
- Python version 3.11
- Java 

## Setup
- Clone repository and move to the cloned directory.
- Run `brew install gunplot`

## NOTE
- Should be run on bash terminal

## Challenge - Echo
- In root directory run: `source ./maelstrom/maelstrom.sh test -w echo --bin ./echo/solution.py --node-count 1 --time-limit 10`

## Challenge - Unique-id
- In root directory run: `source ./maelstrom/maelstrom.sh test -w unique-ids --bin ./uid/solution.py --time-limit 30 --rate 1000 --node-count 3 --availability total --nemesis partition`

## Challenge - Broadcast
- In root directory run for single node cluster: `source ./maelstrom/maelstrom.sh test -w broadcast --bin ./broadcast/solution.py --node-count 1 --time-limit 20  --rate 10`
- In root directory run for multi node cluster: `source ./maelstrom/maelstrom.sh test -w broadcast --bin ./broadcast/solution.py --node-count 5 --time-limit 20  --rate 10`

## Results
- Refer store directory for results
