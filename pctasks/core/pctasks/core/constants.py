# Default table names

DEFAULT_IMAGE_KEY_TABLE_NAME = "imagekeys"
DEFAULT_WEBHOOKS_TABLE_NAME = "webhooks"
DEFAULT_BLOB_TRIGGER_REGISTRATION_TABLE_NAME = "blobtriggerregistrations"

# Default queue names
DEFAULT_INBOX_QUEUE_NAME = "inbox"
DEFAULT_SIGNAL_QUEUE_NAME = "tasksignals"
DEFAULT_WORKFLOW_QUEUE_NAME = "workflows"
DEFAULT_NOTIFICATIONS_QUEUE_NAME = "notifications"
DEFAULT_STORAGE_EVENTS_QUEUE_NAME = "storage-events"
DEFAULT_INGEST_QUEUE_NAME = "ingest"

# Default log container
DEFAULT_LOG_CONTAINER = "tasklogs"
DEFAULT_TASK_IO_CONTAINER = "taskio"
DEFAULT_CODE_CONTAINER = "code"

# Message types
TASK_SUBMIT_MESSAGE_TYPE = "Task"
WORKFLOW_SUBMIT_MESSAGE_TYPE = "Workflow"
NOTIFICATION_MESSAGE_TYPE = "Notification"
EVENTGRID_MESSAGE_TYPE = "EventGrid"

# Settings
SETTINGS_DIR_ENV_VAR = "PCTASKS_SETTINGS_DIR"
SETTINGS_ENV_DIR = "~/.pctasks"
DEFAULT_PROFILE = "default"
ENV_VAR_PCTASK_PREFIX = "PCTASKS_"
ENV_VAR_PCTASKS_PROFILE = "PCTASKS_PROFILE"

ENV_VAR_TASK_APPINSIGHTS_KEY = "PCTASK_APPINSIGHTS_INSTRUMENTATIONKEY"

MICROSOFT_OWNER = "microsoft"

# Schema versions

WORKFLOW_SCHEMA_VERSION = "1.0.0"
TASK_CONFIG_SCHEMA_VERSION = "1.0.0"
TASK_RUN_CONFIG_SCHEMA_VERSION = "1.0.0"
TASK_RESULT_SCHEMA_VERSION = "1.0.0"
TASK_RUN_SIGNAL_SCHEMA_VERSION = "1.0.0"

RECORD_SCHEMA_VERSION = "1.0.0"

# Target environment
DEFAULT_TARGET_ENVIRONMENT = "default"

# Azurite environment
AZURITE_STORAGE_ACCOUNT_ENV_VAR = "AZURITE_STORAGE_ACCOUNT"
AZURITE_HOST_ENV_VAR = "AZURITE_HOST"
AZURITE_PORT_ENV_VAR = "AZURITE_PORT"

# CosmosDB emulator environment
COSMOSDB_EMULATOR_HOST_ENV_VAR = "COSMOSDB_EMULATOR_HOST"
COSMOSDB_EMULATOR_PORT_ENV_VAR = "COSMOSDB_EMULATOR_PORT"
