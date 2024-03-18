<script setup lang="ts">
import {ref} from "vue"
    var inputtype=ref(1)
    var filePath=ref("")
</script>

<template>
    <div>
        <div style="font-size:50px;background-color: rgba(255, 255, 255, 0.5) ;border-radius: 10px;text-align: left;">
        <el-row style="font-family:Microsoft YaHei UI;font-size:35px;">
            <el-col :span="1">
            </el-col>
            <el-col :span="4">
                <span style="font-weight: 800;">
                    Dispatch
                </span>
            </el-col>
            <el-col :span="3">
            </el-col>
            <el-col :span="10">
                <el-radio-group v-model="inputtype" class="ml-4">
                    <el-radio value="1" size="large">Video input</el-radio>
                    <el-radio value="2" size="large">Image input</el-radio>
                </el-radio-group>
                
            </el-col>
            <el-col :span="6">
                <el-button>
                    submit
                </el-button>
            </el-col>
        </el-row>
        <el-row>
            <el-col :span="8">
            </el-col>
            <el-col :span="8">
                <el-input placeholder="文件夹名称" v-model="filePath">
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
            <el-col :span="23">
                <span style="font-weight: 800;">
                    Input Info todo :
                    展示图片总数量,服务的uid
                </span>
            </el-col>
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