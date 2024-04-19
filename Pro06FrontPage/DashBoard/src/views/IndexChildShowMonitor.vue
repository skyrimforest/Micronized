<script setup lang="ts">
import { ref, provide } from "vue"
import axios from "axios";
import APIS_PRO03 from "../utils/api_pro03";
import APIS_PRO04 from "../utils/api_pro04";
import { ElNotification } from "element-plus";
import { useRouter } from "vue-router";

const router = useRouter();
// echarts的引入
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
    TitleComponent,
    TooltipComponent,
    LegendComponent
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";

use([
    CanvasRenderer,
    PieChart,
    TitleComponent,
    TooltipComponent,
    LegendComponent
]);

const option = ref({
    tooltip: {
        trigger: "item",
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: "vertical",
        left: "left",
        data: ["Other", "Learning"]
    },
    series: [
        {
            name: 'Learning Ratio',
            type: "pie",
            radius: ['40%', '70%'],
            data: [
                { value: 8, name: "Other", itemStyle: { color: "#aaaaaa" } },
                { value: 13, name: "Learning", itemStyle: { color: "#000000" } },
            ],
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: "rgba(0, 0, 0, 0.5)"
                }
            }
        }
    ]
});

const value = ref(1);
var estimateinfo = ref([])
const imageinfo = ref([
    { id: 1, url: 'http://localhost:12002/showpics/manin640480100.jpg' },
    { id: 2, url: 'http://localhost:12002/showpics/manin640480101.jpg' }
])
const activeIndex = ref(1)
function getpics() {
    axios.get(APIS_PRO03.pro03getimainfo)
        .then(res => {
            imageinfo.value = res.data
            console.log(imageinfo.value)
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
function jump2Status() {
    router.push("status")
}
function jump2Config() {
    router.push("config")
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
                        Monitor
                    </span>
                </el-col>
                <el-col :span="3">
                </el-col>
                <el-col :span="6">
                    <!-- 触发检测开始 -->
                    <el-button @click="getpics">
                        Show Monitor
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
                <el-col :span="14">
                    <div style="line-height:30%;"><br /></div>
                    <!-- card 1 -->
                    <el-card>
                        <template #header>
                            <div class="card-header" style="line-height: 15px;font-size: 20px;">
                                Critical Frame:
                            </div>
                        </template>
                        <!-- 走马灯 -->
                        <el-carousel height="600px" motion-blur indicator-position="none">
                            <el-carousel-item v-for="item in imageinfo" :key="item.id">
                                <el-image style="width: 1000px;height: 600px;" :src="item.url" fit="cover" />
                            </el-carousel-item>
                        </el-carousel>
                        <template #footer>
                            <el-switch v-model="value" size="large" active-text="Open Monitor"
                                inactive-text="Close Monitor" />
                        </template>
                    </el-card>
                </el-col>
                <el-col :span="1"></el-col>
                <el-col :span="7">
                    <div style="line-height:30%;"><br /></div>
                    <el-row>
                        <div style="line-height:30%;"><br /></div>
                        <!-- card 1 -->
                        <el-col>
                            <el-card>
                                <template #header>
                                    <div class="card-header" style="line-height: 15px;font-size: 20px;">
                                        Learning Ratio:
                                    </div>
                                </template>
                                <!-- ECharts图表 -->
                                <v-chart class="chart" :option="option" />
                            </el-card>
                        </el-col>
                    </el-row>
                    <el-row>
                        <div style="line-height:30%;"><br /></div>
                        <!-- card 1 -->
                        <el-col>
                            <el-card>
                                <template #header>
                                    <div class="card-header" style="line-height: 15px;font-size: 20px;">
                                        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal">
                                            <el-menu-item index="1" @click="jump2Status">System Status</el-menu-item>
                                            <el-menu-item index="2" @click="jump2Config">Current Config</el-menu-item>
                                        </el-menu>
                                    </div>
                                </template>
                                <router-view>
                                </router-view>
                                <!-- 两个信息页面 -->
                            </el-card>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>

            <el-row></el-row>
        </div>
    </div>

</template>



<style scoped>
.chart {
    height: 300px;
}

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