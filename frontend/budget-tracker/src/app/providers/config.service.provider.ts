import { ConfigService } from "../services/config.service";
import { APP_INITIALIZER } from "@angular/core";

function configServiceFactory(config: ConfigService){
    return () => config.loadConfig().toPromise()
}

export const ConfigServiceProvider = {
    provide: APP_INITIALIZER,
    useFactory: configServiceFactory,
    deps: [ConfigService],
    multi: true,
}
