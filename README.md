# nve-rsync-host-monitor-test

Rsync monitoring component: rsync monitor (Test Version). \
This repo is a part of Rsync Monitoring Project: \
["nve-rsync-monitor-project"](https://github.com/drvicx/nve-rsync-monitor-project/)

## Features
- REST API displays basic Status and Hello messages
- Created for deployment tests

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Сервер M (Monitoring)                        │
│            https://notcloud.ru/apps/esrn-rsync-monitoring/          │
│                                                                     │
│   ┌─────────────┐    ┌───────────────┐ [messages] Table             │
│   │   FastAPI   │    │   SQLite DB   │  message                     │
│   │  (main.py)  │◄──►│    data.db    │  --                          │
│   └─────────────┘    └───────────────┘  Hello from RSync Monitoring │
│          ▲                                                          │
│          │                                                          │
│          │                                                          │
│    ┌─────┴──────┐                                                   │
│    │  REST API  │                                                   │
│    └────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
           ▲
           │ GET /api/status
           │ GET /api/data
     ┌─────┴─────┐
     │           │
┌────┴────┐ ┌────┴────┐
│  curl   │ │ Browser │
└─────────┘ └─────────┘

```

## REST API JSON Response (example)

```
Request.: 
            GET https://notcloud.ru/apps/esrn-rsync-monitoring/
            curl -s https://notcloud.ru/apps/esrn-rsync-monitoring/ | jq '.'
Response:
            {
               "service": "RSync Monitoring",
               "version": "1.0.0",
               "endpoints": {
                  "/api/status": "Checks service status",
                  "/api/data": "Retrieves monitoring data from DB"
               }
            }

--
Request.: 
            GET https://notcloud.ru/apps/esrn-rsync-monitoring/api/data
            curl -s https://notcloud.ru/apps/esrn-rsync-monitoring/api/data | jq '.'
Response:
            {
               "message": "Hello from RSync Monitoring",

               "serverInfo": {
                  "currentTS": "2026-06-27T11:00:02",
                  "osVersion": "Ubuntu 24.04 LTS",
                  "osKernel": "6.8.0-124-generic"
               }
            }

--
Request.: 
            GET https://notcloud.ru/apps/esrn-rsync-monitoring/api/status
            curl -s https://notcloud.ru/apps/esrn-rsync-monitoring/api/status | jq '.'
Response:
            {
               "status": "OK",
               "code": 200
            }

```

## Structure && Development steps

```
nve-rsync-host-monitor-test/
│
├── app/
│   ├── __init__.py                 ## step-015
│   ├── main.py                     ## step-009
│   ├── database.py                 ## step-003
│   ├── models.py                   ## step-004
│   ├── schemas.py                  ## step-005
│   │
│   └── routers/                    ## step-006
│       ├── __init__.py             ## step-016
│       ├── status.py               ## step-007
│       └── data.py                 ## step-008
│
├── data/                           ## step-002
│   └── data.db (auto create)       ## step-003
│
├── logs/                           ## step-017
│   ├── err.log                     ## step-018
│   └── out.log                     ## step-019
│
├── scripts/                        ## step-010
│   ├── install.sh                  ## step-011
│   └── run.sh                      ## step-012
│
├── systemd/                        ## step-013
│   └── nve-rsync-monitor.service   ## step-014
│
├── requirements.txt                ## step-001
│
├── .gitignore                      ## step-020
├── LICENSE
└── README.md                       ## step-000

```
