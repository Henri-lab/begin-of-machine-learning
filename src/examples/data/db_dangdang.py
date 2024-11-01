import psycopg2
import json
import datetime

# Load data from external JSON file
with open('dangdang.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Database connection
connection = psycopg2.connect(
    host='localhost',
    user='henrifox',
    password='postgres',
    dbname='crawl_demo',
    options="-c search_path=public"
)

try:
    with connection.cursor() as cursor:
        # Insert metadata into dangdang_metadata
        metadata_sql = """
        INSERT INTO dangdang_metadata (author, source, count, time)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """
        metadata_values = (data["author"], data["source"], data["count"], data["time"])
        cursor.execute(metadata_sql, metadata_values)
        metadata_id = cursor.fetchone()[0]  # Get the last inserted id for linking books

        # Insert each book entry into dangdang_books
        book_sql = """
        INSERT INTO dangdang_books (metadata_id, rank, image, title, recommend, author, times, price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        for book in data["list"]:
            book_values = (
                metadata_id,
                int(book["rank"]),
                book["image"],
                book["title"],
                book["recommend"],
                book["author"],
                book["times"],
                book["price"]
            )
            cursor.execute(book_sql, book_values)

    # Commit transaction
    connection.commit()
finally:
    connection.close()

print("Data inserted successfully!")

