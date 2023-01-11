import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { map } from "rxjs";

@Injectable({
    providedIn: "root",
})
export class ConfigService {
    private gqlHttp = ""
    private gqlWs = ""

    constructor(private http: HttpClient) {}

    get getGqlHttp(): string {
        return this.gqlHttp
    }

    get getGqlWs(): string {
        return this.gqlWs
    }

    setGqlHttp(gqlHttp: string) {
        this.gqlHttp = gqlHttp
    }

    setGqlWs(gqlWs: string) {
        this.gqlWs = gqlWs
    }

    loadConfig() {
        return this.getConfig()
    }

    set(json: {
        gqlHttp: string,
        gqlWs: string,
    }){
        this.setGqlHttp(json.gqlHttp)
        this.setGqlWs(json.gqlWs)
    }

    getConfig() {
        return this.http.get<{
            gqlHttp: string;
            gqlWs: string;
        }>("/budget_tracker_config/budget_tracker_settings.json").pipe(
            map((json) => {
                this.set(json)
                return json
            }),
        )
    }
}