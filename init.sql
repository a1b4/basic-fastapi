-- Initialize database for basic-fasapi application
-- This script runs when the PostgreSQL container starts for the first time

-- Enable UUID extension for PostgreSQL
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create the users table if it doesn't exist
-- Note: This is a backup in case SQLAlchemy doesn't create it automatically
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password_hash VARCHAR NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create index for better performance on username lookups
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);

-- Create index for better performance on email lookups
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Grant necessary permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO fasapi_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO fasapi_user;
