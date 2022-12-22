import uvicorn
import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from context import  BudgetTrackerManager
from mutations import Mutation
from querys import Query


app = FastAPI()
schema = strawberry.Schema(Query, Mutation)

@app.on_event("startup")
async def startup_event() -> None:
    manager: BudgetTrackerManager = BudgetTrackerManager(users={})
    graphql_app = GraphQLRouter(schema, context_getter=manager.get_context)

    app.include_router(graphql_app, prefix="/graphql")

uvicorn.run(app, host="localhost", port=8000)
