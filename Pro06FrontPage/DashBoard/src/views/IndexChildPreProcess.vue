<script setup lang="ts">
import axios from "axios"
import { ref } from "vue"
import APIS_PRO01 from "../utils/api_pro01"
import APIS_PRO04 from "../utils/api_pro04";
import { ElNotification } from "element-plus";
var inputtype = ref(1)
var filePath = ref<string>("")
var imageinfo = ref(
    // [{
    // "id": 1,
    // "uuid": "aptx4869",
    // "count": 233,
    // "total_time": 23,
    // "start_time": "24/3/11 22:30:11"
    // }]
)
function send_pic_name() {
    axios.post(APIS_PRO01.pro01sendpics,
        { filePath: filePath.value })
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
    axios.get(APIS_PRO04.pro04getpicinfo)
        .then(res => {
            console.log(res)
            imageinfo.value=res.data.data
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
                <!-- 标题1 -->
                <el-col :span="4">
                    <span style="font-weight: 800;">
                        System Input
                    </span>
                </el-col>
                <el-col :span="3">
                </el-col>

                <!-- 触发系统开始 -->
                <el-col :span="6">
                    <el-button @click="send_pic_name">
                        submit
                    </el-button>
                </el-col>
                <el-col :span="10">
                    <el-radio-group v-model="inputtype" class="ml-4">
                        <el-radio value="1" size="large">Video input</el-radio>
                        <el-radio value="2" size="large">Image input</el-radio>
                    </el-radio-group>

                </el-col>

            </el-row>
            <el-row>
                <el-col :span="8">
                </el-col>
                <el-col :span="8">
                    <el-input placeholder="Directory Name" v-model="filePath">
                    </el-input>
                </el-col>
            </el-row>
        </div>
        <el-row>

        </el-row>
        <div style="font-size:50px;background-color: rgba(255, 255, 255, 0.5) ;border-radius: 10px;text-align: left;">
            <el-row style="font-family:Microsoft YaHei UI;font-size:35px;">
                <el-col :span="1">
                </el-col>
                <!-- 标题2 -->
                <el-col :span="7">
                    <span style="font-weight: 800;">
                        Input Infomation :
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
                    <!-- 预处理信息表 -->
                    <el-scrollbar height="50vh">
                        <el-table :data="imageinfo" style="width: 100%">
                            <el-table-column type="index"/>
                            <el-table-column prop="uuid" label="uid" />
                            <el-table-column prop="count" label="count" />
                            <el-table-column prop="total_time" label="time cost" />
                            <el-table-column prop="start_time" label="start time" />
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