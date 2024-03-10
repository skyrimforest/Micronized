<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();
function jump2test() {
  router.push("test")
}
function jump2preprocess(){
  router.push("preprocess")
}
function jump2detection(){
  router.push("detection")
}
function jump2estimation(){
  router.push("estimation")
}
function jump2dispatch(){
  router.push("dispatch")
}
</script>

<template>
  <div class="common-layout">
    <el-container>
      <!-- 标头 -->
      <el-header style="font-family:Microsoft YaHei UI;text-align: right; font-size: 30px">
        <el-row>
          <!-- 系统标题 -->
          <el-col :span="8" style="text-align: left">
            <span style="font-size: 40px">Skyrim DashBoard</span>
          </el-col>

          <!-- 系统用户标识 -->
          <el-col :span="16">
            <div class="toolbar" style="text-align:right">
              <el-dropdown>
                <el-icon :size="30" color="white" style="margin-right: 10px;margin-top: 3px">
                  <Setting />
                </el-icon>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item @click="onclick_back">FeedBack</el-dropdown-item>
                    <el-dropdown-item @click="onclick_quit">Log Out</el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
              <el-icon>
                <Avatar />
              </el-icon>
              <span>Admin</span>
            </div>
          </el-col>
        </el-row>
      </el-header>


      <el-container>
        <!-- 侧边栏 -->
        <el-aside width="200px">
          <el-menu>
            <!-- 预处理 -->
            <el-sub-menu index="1" @click="jump2preprocess">
              <template #title>
                <el-icon>
                  <DArrowRight />
                </el-icon>
                <span style="font-size: 20px;">Video and Images PreProcess</span>
              </template>
            </el-sub-menu>

            <!-- 监测 -->
            <el-sub-menu index="2" @click="jump2detection">
              <template #title>
                <el-icon>
                  <DArrowRight />
                </el-icon>
                <span style="font-size: 20px">Face Detection</span>
              </template>
            </el-sub-menu>

            <!-- 预测 -->
            <el-sub-menu index="3" @click="jump2estimation">
              <template #title>
                <el-icon>
                  <DArrowRight />
                </el-icon>
                <span style="font-size: 20px">Pose Estimation</span>
              </template>
            </el-sub-menu>

            <!-- 调度 -->
            <el-sub-menu index="4" @click="jump2dispatch">
              <template #title>
                <el-icon>
                  <DArrowRight />
                </el-icon>
                <span style="font-size: 20px">Docker Dispatch</span>
              </template>
            </el-sub-menu>

            <!-- 测试 -->
            <el-sub-menu index="4" @click="jump2test">
              <template #title>
                <el-icon>
                  <DArrowRight />
                </el-icon>
                <span style="font-size: 20px">测试页面</span>
              </template>
            </el-sub-menu>

          </el-menu>


        </el-aside>

        <!-- 主体部分 -->
        <el-main style="overflow: clip ;line-height:80px;">
          <router-view>
          </router-view>
        </el-main>

      </el-container>
    </el-container>
  </div>

</template>



<style scoped>
.common-layout {
  width: 100%;
  height: 100vh;
  position: fixed;
  background-size: cover !important;
}

.el-container {
  height: 100%;
}

.el-header {
  background-color: rgba(0, 0, 0, 1);
  color: white;
  text-align: center;
  margin: 0 0 0 0;
}

.el-aside {
  width: 410px;
  background-color: rgba(255, 255, 255, 1);
  color: white;
  margin: 0 0 0 0;
}

.el-main {
  background-color: rgba(233, 238, 243, 0.8);
  color: #333;
  text-align: center;
  line-height: 160px;
}

.el-menu {
  text-line-through-color: white;

}

.el-sub-menu {
  background-color: #cccccc;
  border-top: 1px solid grey;
  background-color: rgba(255, 255, 255, 1);
  text-align: center;
}

.el-menu-item {
  margin-left: 30px;
  border-top: 1px solid grey;

}

.common-layout .toolbar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  right: 20px;
}
</style>
