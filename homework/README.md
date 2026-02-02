# Module #2: Homework

## Solution #1:

![Screenshot](Screenshot2026-02-01232906.png)

## Solution #2:

![Screenshot](Screenshot2026-02-01233033.png)

## Solution #3, #4 & #5:

A Python script was created that iterates through each month, downloads the specified CSV file, counts the rows, and adds them to the total.

Script: [row_counter.py](row_counter.py)

## Solution #6:

```yaml
triggers:
  - id: daily_schedule
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "0 9 * * *"   # Runs at 9:00 AM
    timezone: America/New_York

```
