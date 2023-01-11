import { InMemoryCache, from } from "@apollo/client/core";
import { APOLLO_OPTIONS } from "apollo-angular";
import { createClient } from "graphql-ws"
import { RetryLink } from "@apollo/client/link/retry";
import { GraphQLWsLink } from "@apollo/client/link/subscriptions"

import { ConfigService } from "../services/config.service";

function apolloFactory(configService: ConfigService) {
    const client = createClient({
        url: configService.getGqlWs
    })

    return {
        link: from([new RetryLink(), new GraphQLWsLink(client)]),
        cache: new InMemoryCache(),
    }
}

export const apolloServiceProvider = {
    provide: APOLLO_OPTIONS,
    useFactory: apolloFactory,

    deps: [ConfigService],
}
