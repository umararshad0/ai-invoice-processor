# AI Invoice Processor

An AI-powered invoice processing API built with **FastAPI, Amazon Bedrock, PostgreSQL, and Docker Compose**. The application accepts PDF invoices, extracts their text, uses an Amazon Bedrock model to identify invoice information, validates the extracted data, detects potential duplicates, and stores invoice records for human review.

This project demonstrates backend API development, AI integration, database persistence, automated testing, containerization, infrastructure as code, and CI/CD practices.

## Screenshots

![AI Invoice Processor architecture diagram](docs/screenshots/ai-invoice-processor-architecture.png)

### API documentation
![API documentation](docs/screenshots/api-documentation.png)

### Invoice list
![Invoice list](docs/screenshots/invoice-list.png)

### Invoice details
![Invoice list with details](docs/screenshots/invoice-list-details.png)

### Duplicate detection
![Duplicate detection](docs/screenshots/duplicate-detection.png)

### Human review workflow
![Human review workflow](docs/screenshots/human-review-workflow.png)

### CI pipeline passing
![GitHub Actions passing](docs/screenshots/github-actions-passing.png)

## Features

- **PDF invoice upload:** Accepts PDF files through a REST API.
- **PDF validation:** Checks file type, PDF content, and file size before processing. Maximum upload size is 10 MB.
- **Text extraction:** Extracts text from uploaded PDF invoices using `pypdf`.
- **AI-powered extraction:** Uses Amazon Bedrock Converse to extract structured invoice information.
- **Data validation:** Validates extracted invoice information before persistence.
- **Duplicate detection:** Identifies potential duplicate invoices and flags them for review.
- **PostgreSQL persistence:** Stores invoice records in a relational database using SQLAlchemy.
- **Human review:** Supports approval and rejection of invoices.
- **Review protection:** Prevents approval when an invoice requires review.
- **REST API documentation:** Provides interactive API documentation through FastAPI.
- **Automated tests:** Uses pytest with an isolated SQLite test database and mocked external dependencies.
- **Containerization:** Runs the application and PostgreSQL using Docker Compose.
- **Database migrations:** Uses Alembic to manage database schema changes.
- **Continuous integration:** GitHub Actions runs the automated tests and validates the Terraform configuration.

### Architecture Diagram

![AI Invoice Processor Architecture](docs/screenshots/ai-invoice-processor-architecture.png)

## Architecture

The application follows this processing workflow:

1. A client uploads a PDF invoice through the FastAPI endpoint.
2. The API validates the uploaded file.
3. `pypdf` extracts the invoice text.
4. Amazon Bedrock processes the extracted text and returns structured invoice information.
5. The application validates the extracted information and checks for potential duplicates.
6. SQLAlchemy stores the invoice record in PostgreSQL.
7. The invoice can be retrieved and reviewed through the API.
8. An authorized user can approve or reject the invoice through the review endpoint.

### Technology stack

| Component | Technology |
|---|---|
| Backend API | FastAPI |
| Programming language | Python |
| AI integration | Amazon Bedrock Converse |
| AI model | Amazon Nova Micro inference profile |
| PDF processing | pypdf |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database migrations | Alembic |
| Testing | pytest |
| Test database | SQLite |
| Containers | Docker and Docker Compose |
| Infrastructure as code | Terraform |
| CI/CD | GitHub Actions |

## Application Screenshots

### API documentation


FastAPI interactive documentation showing the available API endpoints.

### Invoice list


Example of invoice records retrieved through the API.

### Approved invoice details


Example of an invoice record with its extracted information and approval status.

### Duplicate detection


Example of duplicate invoice detection and review handling.

### Human review workflow


Example of the invoice review and approval workflow.

### GitHub Actions CI


Successful GitHub Actions workflow run.

![API Documentation](docs/screenshots/api-documentation.png)

![Invoice List](docs/screenshots/invoice-list.png)

![Approved Invoice Details](docs/screenshots/invoice-list-details.png)

![Duplicate Detection](docs/screenshots/duplicate-detection.png)

![Human Review Workflow](docs/screenshots/human-review-workflow.png)

![GitHub Actions CI](docs/screenshots/github-actions-passing.png)

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/invoices/upload` | Upload and process a PDF invoice |
| GET | `/invoices/` | Retrieve invoice records |
| GET | `/invoices/{invoice_id}` | Retrieve an individual invoice |
| POST | `/invoices/{invoice_id}/review` | Approve or reject an invoice |

### Interactive API documentation

When the application is running, open:

- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

## Local Development

### Requirements

- Python 3.12
- PostgreSQL
- Docker Desktop and Docker Compose
- AWS account with access to Amazon Bedrock
- AWS credentials configured locally for Bedrock access

### Clone the repository

```bash
git clone https://github.com/umararshad0/ai-invoice-processor.git
cd ai-invoice-processor
```

### Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create your local environment configuration using the project's example configuration:

```bash
cp .env.example .env
```

Update the values in `.env` to match your local database and AWS configuration. Keep real credentials and secrets out of Git.

### Run database migrations

```bash
alembic upgrade head
```

### Start the application

```bash
uvicorn app.main:app --reload
```

The API is available at the address printed by Uvicorn. The Docker Compose setup described below uses port `8001` on the host.

## Docker Compose

Docker Compose runs the FastAPI application and PostgreSQL database as separate services.

Start the services:

```bash
docker compose up --build -d
```

Check service status:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f web
```

View database logs:

```bash
docker compose logs -f db
```

Check the API:

```bash
curl http://localhost:8001/health
```

Open the interactive documentation:

`http://localhost:8001/docs`

Stop the services:

```bash
docker compose down
```

To remove the Compose volumes as well, use `docker compose down -v`. This deletes the persisted database data.

## Database Migrations

Alembic manages database schema changes.

Apply migrations:

```bash
alembic upgrade head
```

Check whether the SQLAlchemy models and migration history are synchronized:

```bash
alembic check
```

## Testing

The automated tests use pytest, an isolated in-memory SQLite database, and mocked external dependencies.

Run the test suite:

```bash
pytest -v
```

The tests cover application behavior without requiring a live Amazon Bedrock invocation.

The project test suite has passed locally, with **15 tests passing**.

## AWS Bedrock Integration

The application uses Amazon Bedrock Converse to process extracted invoice text and return structured invoice information.

The project was tested with Amazon Bedrock using configured AWS credentials. The Docker test setup mounts local AWS credentials into the application container for development.

For a production deployment, an EC2 IAM role should be used instead of mounting local credentials. The required Bedrock permissions and inference profile access must be verified before deployment.

## Infrastructure as Code

The `terraform/` directory contains infrastructure configuration for a planned AWS deployment.

The configuration includes:

- Amazon Linux 2023 ARM64 EC2 instance.
- `t4g.micro` instance type.
- IAM instance profile.
- Security group configuration.
- Encrypted 8 GB gp3 root volume.
- AWS provider configuration for the `eu-north-1` region.

Terraform formatting and validation are included in the CI workflow.

**Deployment status:** The Terraform configuration has been formatted and validated locally and through CI. AWS infrastructure has not been provisioned by this project. No Terraform apply has been performed.

## Continuous Integration

GitHub Actions runs automated checks when changes are pushed to the repository or pull requests target the `main` branch.

The workflow includes two jobs:

### Python tests

- Sets up Python 3.12.
- Installs project dependencies.
- Runs the pytest test suite.
- Uses a test database and placeholder configuration.
- Does not invoke Amazon Bedrock or require AWS credentials.

### Terraform validation

- Sets up Terraform.
- Checks formatting using `terraform fmt -check -recursive`.
- Initializes Terraform without configuring a remote backend.
- Validates the Terraform configuration.

The workflow does not run `terraform plan` or `terraform apply`, and it does not provision AWS resources.

## Security Considerations

- PDF uploads are checked before processing.
- File size is limited to 10 MB.
- Database operations use SQLAlchemy.
- Real credentials should be stored outside the repository.
- `.env` files containing secrets should not be committed.
- Production AWS access should use IAM roles rather than long-lived local credentials.
- Human review is required for invoices flagged for review.

## Current Limitations

- Invoice extraction depends on the quality and readability of the uploaded PDF.
- AI-extracted information requires validation.
- Potential duplicates require human review.
- The application currently provides API-based review rather than a separate frontend interface.
- AWS deployment has not yet been performed.
- Production IAM permissions and Bedrock inference profile access still require deployment verification.

## Project Status

The project has been tested locally and through Docker Compose.

Verified functionality includes:

- PDF upload and validation.
- PDF text extraction.
- Amazon Bedrock invoice extraction.
- Extracted data validation.
- Duplicate detection.
- PostgreSQL persistence and retrieval.
- Human approval and rejection workflow.
- Alembic migration checks.
- Automated pytest suite.
- Docker Compose end-to-end workflow.
- Terraform formatting and validation.
- GitHub Actions CI workflow.

The Docker Compose end-to-end test successfully uploaded an invoice, processed and persisted its information, retrieved the record, and approved it through the review endpoint.

**AWS infrastructure deployment remains pending.**

## Repository

GitHub: https://github.com/umararshad0/ai-invoice-processor
