import PREFIXES  from "./device";
const URL_PREFIX = PREFIXES.CLOUD_PREFIX+":12002/";
// const URL_PREFIX = PREFIXES.LOCAL_PREFIX+":12002/";
const APIS_PRO03:{[key:string]:string} = {
    pro03estimatestart:"estimate/draw",
    pro03estimateshow:"estimate/result",
    pro03getimainfo:"getpicinfo",
    pro03showima:"showpics",
}

for (const i in APIS_PRO03) {
    APIS_PRO03[i] = URL_PREFIX + APIS_PRO03[i];
}

export default APIS_PRO03

