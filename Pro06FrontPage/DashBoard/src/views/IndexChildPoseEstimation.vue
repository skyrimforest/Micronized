<script setup lang="ts">
import { ref } from "vue"
import axios from "axios";
import APIS_PRO03 from "../utils/api_pro03";
import APIS_PRO04 from "../utils/api_pro04";
import { ElNotification } from "element-plus";
var estimateinfo = ref([
])
let dialogVisible=ref(0)
let url=ref("")
function getpics(index: number) {
    dialogVisible.value=1;
    url.value=APIS_PRO03.pro03estimateshow + "/" + estimateinfo.value[index].image_name
}
function start_estimation() {
    axios.post(APIS_PRO03.pro03estimatestart)
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
function get_db_info() {
    axios.get(APIS_PRO04.pro04getestimateinfo)
        .then(res => {
            console.log(res)
            estimateinfo.value = res.data.data
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
    <el-dialog v-model="dialogVisible" title="Tips" width="500">
        <el-image style="width: 200px; height: 200px" :src="url" fit="contain" />
        <template #footer>
            <div class="dialog-footer">
                <el-button @click="dialogVisible = false">Close</el-button>
            </div>
        </template>
    </el-dialog>
    <div>
        <div style="font-size:50px;background-color: rgba(255, 255, 255, 0.5) ;border-radius: 10px;text-align: left;">
            <el-row style="font-family:Microsoft YaHei UI;font-size:35px;">
                <el-col :span="1">
                </el-col>
                <el-col :span="4">
                    <!-- 标题1 -->
                    <span style="font-weight: 800;">
                        Estimation
                    </span>
                </el-col>
                <el-col :span="3">
                </el-col>
                <el-col :span="6">
                    <!-- 触发检测开始 -->
                    <el-button @click="start_estimation">
                        start estimation
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
                        Estimate Info:
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
                        <el-table :data="estimateinfo" style="width: 100%" highlight-current-row>
                            <el-table-column type="index"></el-table-column>
                            <el-table-column prop="uuid" label="uid" />
                            <el-table-column prop="count" label="count" width="80px" />
                            <el-table-column prop="image_name" label="image name" />
                            <el-table-column prop="detected" label="detected" width="80px" />
                            <el-table-column prop="learning" label="learning" width="80px" />
                            <el-table-column prop="total_time" label="total time" width="200px" />
                            <el-table-column prop="start_time" label="start time" />
                            <el-table-column label="show pics">
                                <template #default="scope">
                                    <el-button size="small" @click="getpics((scope.$index))">Detail</el-button>
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-scrollbar>
                </el-col>
                <el-col :span="1"></el-col>
            </el-row>
            <el-row></el-row>
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