<script setup lang="ts">
import { ref, provide } from "vue"

const dvalue = ref('')
const evalue = ref('')
const rvalue = ref('')
const doptions = ref([
    {
        value: 'RFBNet',
        label: 'RFBNet',
    }
])
const eoptions = ref([
    {
        value: 'HopeNetLite',
        label: 'HopeNetLite',
    }
])
const roptions = ref([
    {
        value: '480p',
        label: '480p',
    },
    {
        value: '640p',
        label: '640p',
    },
    {
        value: '1280p',
        label: '1280p',
    },
])
</script>

<template>
    <div style="height: 250px;">
        <el-descriptions title="Current Config" :column="1" border style="line-height:50px ;">
            <!-- 模式选择 -->
            <el-descriptions-item label="Pattern" label-align="right" align="center">
                <el-tag type="primary">Delay Priority</el-tag>
                <el-tag type="success">Edge</el-tag>
            </el-descriptions-item>
            <!-- 模型选择 -->
            <el-descriptions-item label="Detection" label-align="right" align="center">

                <el-select v-model="dvalue" placeholder="Model Select">
                    <el-option v-for="item in doptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>

            </el-descriptions-item>
            <el-descriptions-item label="Estimation" label-align="right" align="center">

                <el-select v-model="evalue" placeholder="Model Select">
                    <el-option v-for="item in eoptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>

            </el-descriptions-item>


            <!-- 视频配置 -->
            <el-descriptions-item label="Resolution" label-align="right" align="center">
                <el-select v-model="rvalue" placeholder="Reso Select">
                    <el-option v-for="item in roptions" :key="item.value" :label="item.label" :value="item.value" />
                </el-select>
             </el-descriptions-item>
        </el-descriptions>
    </div>


</template>
