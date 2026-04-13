import logging
import os

from flask import Flask, jsonify, render_template
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__, template_folder='templates')

log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME", "kmk"),
        user=os.getenv("DB_USER", "kmk_app"),
        password=os.getenv("DB_PASSWORD", "kmk_password"),
        cursor_factory=RealDictCursor,
    )


@app.get("/")
def index():
    return render_template('index.html')


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.get("/api/health")
def api_health():
    return jsonify({"status": "ok"}), 200


@app.get("/api/requests")
def list_requests():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT
                        id,
                        student_id,
                        student_email,
                        requested_days,
                        reason,
                        status,
                        created_at
                    FROM student_extension_requests
                    ORDER BY created_at DESC
                    """
                )
                rows = cur.fetchall()
        return jsonify(rows), 200
    except Exception:
        logger.exception("Failed to fetch extension requests")
        return jsonify({"error": "failed_to_fetch_requests"}), 500


if __name__ == "__main__":
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))
    app.run(host=host, port=port)
