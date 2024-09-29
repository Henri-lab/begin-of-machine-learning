until git push -u origin cv; do
    echo "push branch cv failded ,retry..."
    sleep 1
done
echo "push branch cv successfully"
