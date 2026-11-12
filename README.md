# PayPilotLabs CRM

PayPilotLabs CRM is a sales tool that keeps every lead, deal and customer conversation in one place.

By [PayPilotLabs](https://paypilotlabs.com). Support and requests: https://paypilotlabs.com/roadmap/

## What it does

- Keeps leads, deals, contacts and organisations.
- Shows your sales pipeline as a board, so you can drag a deal from one stage to the next.
- Logs emails, notes and tasks on each record.
- Logs phone calls (Twilio or Exotel settings are built in) and WhatsApp messages.
- Assigns new leads to the right person with assignment rules.
- Tracks response-time targets (SLAs), working days and holidays.
- Runs simple automations, such as sending an email when a record changes.
- Adds company details to a record from its website address (domain enrichment).
- Offers web forms that put new leads straight into the pipeline.
- Shows dashboards, and imports your existing data from a file.
- Handles users, roles and a sales team hierarchy.

## How it helps your business

- No lead gets lost: every enquiry has an owner and a next step.
- You see which deals are stuck, and where in the pipeline they are.
- The whole team sees the full history with a customer: emails, calls and notes.
- Leads get a reply sooner, because response-time targets are tracked.
- Managers see results on a dashboard, with no spreadsheets to merge.

## How it fits with other PayPilotLabs products

PayPilotLabs CRM runs on `paypilotlabs-framework`, the base all PayPilotLabs products share. It needs no other PayPilotLabs product. Phone calls use the Twilio and Exotel settings inside the CRM itself.

## Run it

PayPilotLabs CRM runs as a PayPilotLabs framework v16 site in Docker: MariaDB 11.8, Redis, and an image holding the framework + the CRM.

1. Push this repo and its companions (`paypilotlabs-framework`) to `github.com/paypilotlabs` (private is fine).
2. Build the image: `./docker/build.sh` (while the repos are private: `GITHUB_TOKEN=<token with read access> ./docker/build.sh`; the token is then stored in the image history, so never push that image). It tags `paypilotlabscrm:<git commit>` (push that one to ECR) and `paypilotlabscrm:latest`.
3. Start it: `docker compose -f docker/docker-compose.yml up -d`
4. Watch the first-run setup: `docker compose -f docker/docker-compose.yml logs -f create-site` (wait for it to exit 0).
5. Open http://crm.localhost:8080 and log in as `Administrator` / `admin`. Change the password straight away.

Stop with `docker compose -f docker/docker-compose.yml down` (add `-v` to delete the data).

## Licence

AGPL-3.0. See [LICENSE](LICENSE) for the full terms. Based on open-source work by others; see [NOTICE.md](NOTICE.md) for credits.
