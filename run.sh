SOURCE="${BASH_SOURCE[0]}"
DIR="$( dirname "$SOURCE" )"

python $DIR/converter.py $DIR

read pause