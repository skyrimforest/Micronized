import PREFIXES  from "./device";
const URL_PREFIX = PREFIXES.CLOUD_PREFIX+":12003/";
const APIS_PRO04:{[key:string]:string} = {
    pro04getpicinfo:"collector/imageinfo",
    pro04getdetectinfo:"collector/detectinfo",
    pro04getestimateinfo:"collector/estimateinfo"
}

for (const i in APIS_PRO04) {
    APIS_PRO04[i] = URL_PREFIX + APIS_PRO04[i];
}

export default APIS_PRO04

