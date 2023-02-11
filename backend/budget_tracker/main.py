import strawberry
import uvicorn
from budget_tracker.context import BudgetTrackerManager
from budget_tracker.mutations import Mutation
from budget_tracker.querys import Query
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

app = FastAPI()
schema = strawberry.Schema(Query, Mutation)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event() -> None:
    manager: BudgetTrackerManager = BudgetTrackerManager(budget_trackers={})
    graphql_app = GraphQLRouter(schema, context_getter=manager.get_context)

    app.include_router(graphql_app, prefix="/graphql")

uvicorn.run(app, host="localhost", port=8000)
