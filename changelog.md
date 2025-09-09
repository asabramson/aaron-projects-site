# V1.X - n/a - Changelog Information

I had a lockout issue with my account, and was not able to push any updates for the past month. Due to this, the
entire past month of work will all be listed under one entry (shown below). In the future, commits will be listed
under here in the format "VA.B" with "A" being the project number that I am working on, and "B" being the n'th
commit in that project.

# V2.0 - 9/9/25 - Lasker Morris Game, Catchup from Missing Entries

- Lasker Morris game completely finished
    - AI player program implemented
        - Minimax algorithm with alpha beta pruning was used
        - Maybe add a Monte Carlo Tree Search variant in the future?
    - */laskermorris* (GET) and */move* (POST) routes added
        - */laskermorris* renders the page
        - */move* is used by the frontend to send moves to the backend and get the AI player's move in the response
    - Developed frontend to capture user moves
        - Calls the */move* route
- Functionality for API key protection added
    - Not in use yet, but can be used to block unauthorized POST requests to routes with the "@api_key_required" decorator (will be used in the future)
- New global styles added for buttons and modals
- Wording on error page for 403 code slightly edited
- FUTURE: Add database connection to the Lasker Morris game
    - A DB model already exists (LaskerMorrisStats) which will store the user's total number of games played and win count, it just needs to be wired to the routes