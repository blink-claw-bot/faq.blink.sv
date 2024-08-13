# Set your Blink account as an LNbits funding source

Since LNbits v0.12.10 Blink is available to be set as a funding source in the LNbits Server Settings.\
\
Steps to set up:\
\
\* get a Blink API key at [dashboard.blink.sv](https://dashboard.blink.sv\)). Find more details about the Dashboard and API keys [here](https://dev.blink.sv/api/auth).\
\
\* log in as the [LNbits super user](https://github.com/lnbits/lnbits/blob/dev/docs/guide/admin\_ui.md)

\* open the `Server` settings

![](<../.gitbook/assets/lnbits\_super\_user (1).png>)\


\* choose `Blink` from the dropdown menu under `Funding Sources` **-** `Active Funding (Requires server restart)`\
\* paste your API key to the `Key` field

\
![](../.gitbook/assets/lnbits\_funding\_sources.png)



\* restart LNbits\
&#x20;\
\* alternatively can edit the LNbits `.env` file directly as well if have access to the terminal on the server&#x20;

