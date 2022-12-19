import uvicorn
import strawberry

from typing import List, Dict
from fastapi import FastAPI
from datetime import datetime

from strawberry.types import Info
from strawberry.fastapi import GraphQLRouter


async def get_context() -> Dict:
    return {"users": "users result"}


@strawberry.type
class Budget:
    budget_id: str
    target: float
    amount: float
    percentage: float


@strawberry.type
class Income:
    income_id: str
    pay_cycle: str
    pay_day: datetime
    amount: float


@strawberry.type
class User:
    user_id: str
    income_streams: List[Income]
    budgets: List[Budget]


@strawberry.type
class Query:
    @strawberry.field
    def get_users(self, info: Info) -> User:
        return info.context.items()

#dicts suck add in mongodb for the database


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self, info: Info, user_id: str) -> User:
        info.context[user_id] = User(user_id=user_id, income_streams=[], budgets=[])
        return info.context[user_id]

    @strawberry.mutation
    def add_budget(self, info: Info, user_id: str, target: float, amount: float, percentage: float) -> User:
        info.context[user_id].budgets.append(Budget(budget_id=user_id, target=target, amount=amount, percentage=percentage))
        return info.context[user_id]



schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(
  schema,
  context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")

uvicorn.run(app, host="localhost", port=8000)


# def main():
#     print("Hello World!")

# if __name__ == "__main__":
#     main()