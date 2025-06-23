# Demo notes

## Cloud-hosted solutions

### Confluence

- Similar to Notion.
- Allows for multi user edit on the same files.
- Many templates to work with so that creating new documents can be standardised.
- Confluence setup on google meet
Asana

#### Confluence self-hosted

- Requires a license key.
- Presumably same as Cloud-hosted solution
- EPFL has some form of contract with them?

### Next-Cloud

What products they offer?
1. Next-Cloud Files
File sharing product, can have real-time collaboration (integration with Microsoft Office, Collabora, etc...)
[Demos & Website](https://nextcloud.com/files/)
2. Nextcloud Talk
Conferencing software
[Demos & Website](https://nextcloud.com/talk/)
3. Next-Cloud Groupware
Integrated calendar, mail, contacts, kabana board (todo lists)
[Demos & Website](https://nextcloud.com/groupware/)
4. Nextcloud Office
Microsoft Office suite but it's Nextcloud
[Demos & Website](https://nextcloud.com/office/)

#### Next-Cloud self-hosted

- Offers an all-in-one docker image [Link](https://github.com/nextcloud/all-in-one)
- Only accessible with a AIO key which is acquired through enterprise software.
- In this docker container all products are offered together.

Pricing is free for self-hosted, but for managed services like Nextcloud One, it costs around 13€ per user per month, totaling approximately $4,680 per year for 30 users, billed monthly.

### ownCloud

ownCloud, another open-source file hosting and collaboration platform, mirrors Next-Cloud's functionality, with features like file sharing, real-time collaboration via integrations with **other office suites** (Collabora, ONLYOFFICE, Microsoft Office Online Server), and federated cloud sharing.

Elasticsearch is feasible via plugins

Self-hosted can connect to preexisting databases.
Stored in a MariaDB database so existing files can be connect
Developed at CERN

Pricing is free for self-hosted, but the commercial license costs €15 per user per month, totaling approximately $5,400 per year for 30 users, billed monthly.


### Dropbox Business

DropBox offers file sharing and real-time editing via Dropbox Paper, it also has integrations with tools like Slack and Zoom.

Pricing for the Standard plan is $15 per user per month, totaling $5,400 per year for 30 users, with 5 TB of shared storage, billed monthly. It is cloud-only, with no self-hosting option.

### Slab

Slab is a knowledge base and wiki software, designed for creating, organizing, and sharing documentation, with a focus on knowledge management. It offers real-time collaborative editing, integration with tools like Slack, GitHub, and Google Drive, and a powerful search function.

It is pretty much the same as confluence but **cannot be self-hosted**.

Pricing includes a free plan for up to 10 users, with the Startup plan at $6.67 per user per month (billed annually), totaling approximately $2,401 per year for 30 users, offering a cost-effective option for knowledge sharing.


### Box

Box is a cloud content management platform, providing secure file sharing, real-time collaboration via Box Canvas and Box Notes, and over 1,500 integrations, including Microsoft 365 and Google Workspace. It is user-friendly, with mobile, web, and desktop access, suitable for labs needing to manage and collaborate on large datasets. Collaboration features include co-editing, whiteboarding, and shared workspaces, with AI-powered search enhancing content discovery. Integration with Elasticsearch is possible via APIs, aligning with lab needs for advanced search. Pricing for the Business plan is $20 per user per month, totaling $7,200 per year for 30 users, with unlimited storage, billed monthly, positioning it as a premium option. It is cloud-only, with no self-hosting option.

### Zoho

Pricing includes a Standard plan at $3 per user per month and a Professional plan at $6, totaling $1,080 to $2,160 per year for 30 users, billed monthly, making it the most cost-effective option. It is cloud-only, with no self-hosting option.

