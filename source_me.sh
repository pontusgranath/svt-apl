if [[ $SHLVL -gt 1 ]]; then
    echo "Remember: you need to run me as 'source ./source_me.sh', not execute
it!"
    exit
fi

if [ -d venv ]; then
    source venv/bin/activate
else
    python3 -m venv venv
    source venv/bin/activate
fi

if [ -f .env-normal ]; then
    source .env-normal
fi