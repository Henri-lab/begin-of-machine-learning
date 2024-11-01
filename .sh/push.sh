#!/bin/bashv
branch = "spider"

until git push -u origin "$branch; do
    echo "push branch failded ,retry..."
    sleep 1
done
echo "push branch successfully"
