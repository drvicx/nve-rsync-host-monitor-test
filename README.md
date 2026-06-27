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
           GET https://notcloud.ru/apps/esrn-rsync-monitoring/api/status
Response:
           {
              "status": "OK",
              "code": 200
           }

Request.: 
          GET https://notcloud.ru/apps/esrn-rsync-monitoring/api/data
Response:
          {
             "message": "Hello from RSync Monitoring",

             "serverInfo": {
                "currentTS": "2026-06-27T11:00:02",
                "osVersion": "Ubuntu 24.04 LTS",
                "osKernel": "6.8.0-124-generic"
              }
          }

```
