until git push -u origin b1; do
    echo "push branch b1 failded ,retry..."
    sleep 1
done
echo "push branch cv successfully"
