import PREFIXES  from "./device";
const URL_PREFIX = PREFIXES.CLOUD_PREFIX+":12001/";
const APIS_PRO02:{[key:string]:string} = {
    pro02detectstart:"detect/detectstart",
}

for (const i in APIS_PRO02) {
    APIS_PRO02[i] = URL_PREFIX + APIS_PRO02[i];
}

export default APIS_PRO02

