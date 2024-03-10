<script setup>
  import APIS_PRO01 from "../utils/api_pro01.ts";
  import axios from "axios";

  function click_test(){
    axios.post(APIS_PRO01.pro01test)
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
  function click_send(){
    var data={
      filePath:"handshaking"
    }
    axios.post(APIS_PRO01.pro01sendpics,data)
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
  function click_sendtest(){
    axios.post(APIS_PRO01.pro01sendtest)
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
</script>

<template>
  <el-button @click="click_test">
    点我测试
  </el-button>
  <el-button @click="click_sendtest">
    点我发图测试
  </el-button>
  <el-button @click="click_send">
    点我发图
  </el-button>
</template>

<style scoped>
</style>
