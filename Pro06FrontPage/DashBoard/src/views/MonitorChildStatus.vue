<script setup lang="ts">
import { ref, provide } from "vue"

const cpu_ratio = ref(83)
const bandwidth = ref(2500)
const memory_ratio = ref(76)
const people = ref(21)
const time_cost = ref(376)

</script>

<template>
    <div  style="height: 250px;">
        <el-descriptions title="System Status" :column="2" border>
            <el-descriptions-item label="CPU Ratio" label-align="right" align="center" class-name="cpu">
                {{ cpu_ratio }}%
            </el-descriptions-item>
            <el-descriptions-item label="Bandwidth" label-align="right" align="center">
                {{bandwidth}}kBps
            </el-descriptions-item>
            <el-descriptions-item label="Memory Ratio" label-align="right" align="center">
                {{memory_ratio}}%
            </el-descriptions-item>
            <el-descriptions-item label="People" label-align="right" align="center">
                {{ people }}
            </el-descriptions-item>
            <el-descriptions-item label="Time Cost" label-align="right" align="center">
                {{time_cost}}ms
            </el-descriptions-item>
        </el-descriptions>
    </div>

</template>
