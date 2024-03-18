<script setup lang="ts">
import axios from "axios";
import { ref } from "vue"
import APIS_PRO02 from "../utils/api_pro02";
import APIS_PRO04 from "../utils/api_pro04";
import { ElNotification } from "element-plus";
var detectinfo = ref(
    // [{
    // "id": 1,
    // "uuid": "aptx4869",
    // "count": 233,
    // "image_name": "shaking.png",
    // "boxes": 5,
    // "total_time": 87,
    // "start_time": "24/3/11 22:30:23"
    // }]
)
function start_detection(){
    axios.post(APIS_PRO02.pro02detectstart)
        .then(res => {
            console.log(res)
        })
        .catch(err => {
            console.log(err)
            ElNotification({
                title: 'Error',
                message: '数据请求失败',
                type: 'error',
            })
        })
}
function get_db_info(){
    axios.get(APIS_PRO04.pro04getdetectinfo)
        .then(res => {
            console.log(res)
            detectinfo.value=res.data.data
        })
        .catch(err => {
            console.log(err)
            ElNotification({
                title: 'Error',
                message: '数据请求失败',
                type: 'error',
            })
        })
}
</script>

<template>
    <div>
        <div style="font-size:50px;background-color: rgba(255, 255, 255, 0.5) ;border-radius: 10px;text-align: left;">
            <el-row style="font-family:Microsoft YaHei UI;font-size:35px;">
                <el-col :span="1">
                </el-col>
                <el-col :span="4">
                    <!-- 标题1 -->
                    <span style="font-weight: 800;">
                        Detection
                    </span>
                </el-col>
                <el-col :span="3">
                </el-col>
                <el-col :span="6">
                    <!-- 触发检测开始 -->
                    <el-button @click="start_detection">
                        start detection
                    </el-button>
                </el-col>
            </el-row>
        </div>
        <el-row>

        </el-row>
        <div style="font-size:50px;background-color: rgba(255, 255, 255, 0.5) ;border-radius: 10px;text-align: left;">
            <el-row style="font-family:Microsoft YaHei UI;font-size:35px;">
                <el-col :span="1">
                </el-col>
                <el-col :span="7">
                    <!-- 标题2 -->
                    <span style="font-weight: 800;">
                        Detect Info:
                    </span>
                </el-col>
                <el-col :span="6">
                    <el-button @click="get_db_info">
                        get result
                    </el-button>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="1"></el-col>
                <el-col :span="22">
                    <!-- 每张图的检测信息表 -->
                    <el-scrollbar height="60vh">
                        <el-table :data="detectinfo" style="width: 100%">
                            <el-table-column type="index"/>
                            <el-table-column prop="uuid" label="uid" />
                            <el-table-column prop="count" label="count" width="80px"/>
                            <el-table-column prop="image_name" label="image name" />
                            <el-table-column prop="detected" label="detected" width="100px" />
                            <el-table-column prop="total_time" label="total time" width="200px"/>
                            <el-table-column prop="start_time" label="start time"width=200px />
                        </el-table>
                    </el-scrollbar>
                </el-col>
                <el-col :span="1"></el-col>
            </el-row>
        </div>
    </div>

</template>



<style scoped>
.el-button {
    width: 180px;
    border: 1px solid grey;
    color: black;
}

.el-table {
    border: 1px solid grey;
    color: black;
}

.el-input {
    border: 1px solid grey;
    color: #ffffff
}

.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.el-col {
    border-radius: 4px;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}
</style>