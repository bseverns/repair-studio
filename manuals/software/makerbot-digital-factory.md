# MakerBot Digital Factory / CloudPrint

Cloud control for the Sketch fleet and Method X. This doc captures access, workflow, and reporting habits.

## Why we depend on it
- Central queue for all MakerBot printers, so no USB sneaker-net.
- Live monitoring (camera, temps) lets you kill failing jobs before wasting filament.
- Usage analytics feed monthly reports to leadership without manual spreadsheet pain.

## Access + accounts
- URL: <https://digitalfactory.makerbot.com>
- Ask IT in `#fabrication` for account provisioning. They’ll tie your login to the `FieldKit` organization.
- Printers are grouped by zone: `SKETCH-01`, `SKETCH-02`, `SKETCH-L`, `METHOD-X`. Don’t rename without updating signage + QR codes.

## Job workflow
1. Upload STL/STEP files to a project workspace. Organize by project slug (e.g., `rigging-brackets-2024w32`).
2. Choose the correct printer profile and material. CloudPrint exposes recommended presets; tweak only if you have a reason.
3. Add job notes with filament color, customer, and priority. This keeps the queue self-documenting.
4. Watch the live cam for the first five layers. Pause or cancel if adhesion dies, then document the failure in the job notes and in `data/prints/incidents.csv`.

## Maintenance + reporting
- Archive completed jobs monthly: `Queue` → `Archive`. Keeps dashboards responsive.
- Export analytics quarterly (`Analytics` → `Export CSV`) and stash them in `data/prints/reports/<quarter>.csv`.
- Update material inventory when you load a new Smart Spool; include serial number and install date.

## Troubleshooting
- **Printer offline**: Power cycle printer, then use `Printers` → `Reconnect`. If offline after 5 minutes, ping IT.
- **Stuck job**: Cancel from the queue, then clear the printer’s build plate and purge. Note downtime in `policies/fabrication/uptime-log.md`.
- **SAML login loop**: Clear cookies or use private window. If persistent, open a support ticket via MakerBot portal.

## References
- Knowledge base: <https://support.makerbot.com/s/topic/0TO6S000000Cp6nWAC/cloudprint>
- Admin guide: <https://support.makerbot.com/s/article/1667337554226>
- API docs (for future automation): <https://support.makerbot.com/s/article/CloudPrint-API-Overview>
