# PayPilotLabs CRM

Sales CRM for small teams: leads, deals, contacts and organizations, a Kanban pipeline, email and call logging, tasks and notes.

By [PayPilotLabs](https://paypilotlabs.com). Support and requests: https://paypilotlabs.com/roadmap/

## Run it

PayPilotLabs CRM runs as a Frappe v16 site in Docker: MariaDB 11.8, Redis, and an image holding frappe + crm.

1. Push this repo and its companions (`paypilotlabs-framework`) to `github.com/paypilotlabs` (private is fine).
2. Build the image: `./docker/build.sh` (while the repos are private: `GITHUB_TOKEN=<token with read access> ./docker/build.sh`; the token is then stored in the image history, so never push that image)
3. Start it: `docker compose -f docker/docker-compose.yml up -d`
4. Watch the first-run setup: `docker compose -f docker/docker-compose.yml logs -f create-site` (wait for it to exit 0).
5. Open http://crm.localhost:8080 and log in as `Administrator` / `admin`. Change the password straight away.

Stop with `docker compose -f docker/docker-compose.yml down` (add `-v` to delete the data).
See NOTICE.md for the licence and origin.

## Licence

AGPL-3.0. Based on the open-source Frappe project (crm v16.0.2); see [NOTICE.md](NOTICE.md) for the origin and attribution, and the licence file in this folder for the full terms.
