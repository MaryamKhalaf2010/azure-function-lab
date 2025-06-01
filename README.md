# Azure Functions Lab Project: HttpToQueue & HttpToSql

### name : Maryam Khalaf

This project contains two Azure Functions written in Python:

* **HttpToQueue**: Accepts HTTP POST requests and sends a message to an Azure Storage Queue.
* **HttpToSql**: Accepts HTTP POST requests and inserts data into an Azure SQL Database.

## ✅ Requirements (Pre-requisites)

Make sure you have the following installed/setup:

### Tools:

* [Python 3.10+](https://www.python.org/downloads/)
* [Azure Functions Core Tools v4](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
* [Visual Studio Code](https://code.visualstudio.com/) with Azure Functions extension
* [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* [Azure Storage Explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer/) (for viewing queue messages)
* A GitHub account for code versioning and publishing

### Azure Resources:

* Azure Storage Account (for Queue and AzureWebJobsStorage)
* Azure SQL Server and Database (e.g., `myfunctiondb`)
* Add your public IP to the **SQL Server firewall**
* SQL Table `Person(Name NVARCHAR(100), City NVARCHAR(100))`

---

## ⚙️ Setup Instructions

### 1. Clone the Repo / Create Project

```bash
func init lab-functions --python
cd lab-functions
func new --name HttpToQueue --template "HTTP trigger" --authlevel "anonymous"
func new --name HttpToSql --template "HTTP trigger" --authlevel "anonymous"
```

### 2. Add Output Bindings

Update `function.json` and Python decorators:

* `HttpToQueue` ➜ Azure Queue output binding
* `HttpToSql` ➜ Azure SQL Database output binding

### 3. Set Connection Strings in `local.settings.json`

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "<your-storage-connection-string>",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "SqlConnectionString": "<your-sql-connection-string>"
  }
}
```

---

## ▶️ Run and Test Functions Locally

### Start the Function App:

```bash
func start
```

### Test `HttpToQueue`:

```bash
curl -X POST http://localhost:7071/api/HttpToQueue -H "Content-Type: application/json" -d '{"name": "Maryam"}'
```

### Verify Queue Message:

1. Open **Azure Storage Explorer**
2. Navigate to your storage account > Queues > `myqueue-items`
3. View messages to confirm it was sent

### Test `HttpToSql`:

```bash
curl -X POST http://localhost:7071/api/HttpToSql -H "Content-Type: application/json" -d '{"name": "Maryam", "city": "Ottawa"}'
```

### Verify SQL Insert:

Run the query below in **Query Editor** (Azure Portal) or using SSMS:

```sql
SELECT * FROM Person;
```

---

## 📁 GitHub Publishing

### 1. Initialize Git:

```bash
git init
git add .
git commit -m "Initial commit with working Azure Functions"
```

### 2. Create GitHub Repository:

Go to [GitHub](https://github.com/) and create a new public repo

### 3. Push Code:

```bash
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

---

## 📽️ Demo Video

[\[YouTube demo link here]](https://youtu.be/Bg1PlePtvWg)

---

## 🧠 What I Learned

* How to create and bind output to Azure Storage Queues and Azure SQL DB
* How to run and debug Azure Functions locally
* How to use Azure Storage Explorer to inspect queue messages
* Importance of configuring connection strings and bindings correctly
