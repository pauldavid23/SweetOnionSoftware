CREATE TABLE IF NOT EXISTS extension_requests (
    id SERIAL PRIMARY KEY,
    student_id VARCHAR(50) NOT NULL,
    student_email VARCHAR(255) NOT NULL,
    requested_days INTEGER NOT NULL,
    reason TEXT NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO extension_requests (student_id, student_email, requested_days, reason, status)
VALUES
    ('STU-1001', 'alex@example.com', 7, 'Family emergency', 'pending'),
    ('STU-1002', 'jordan@example.com', 3, 'Medical appointment', 'approved'),
    ('STU-1003', 'casey@example.com', 5, 'Travel disruption', 'pending');