"""Persist the generated upload filename with each invoice.

Revision ID: 20261122_filename
Revises: 0acd141242eb
Create Date: 2026-11-22
"""
from alembic import op
import sqlalchemy as sa


revision = "20261122_filename"
down_revision = "0acd141242eb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("invoices", sa.Column("stored_filename", sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column("invoices", "stored_filename")
