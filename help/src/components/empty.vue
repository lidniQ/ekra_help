<script>
</script>

<template>
  <div class="empty_bd">
    <div class="empty_wrapper">
      <div class="empty_label"> Выберите модуль для просмотра документации </div>
      <div class="empty_icon" style="padding-left: 32px;"> <i class="fa-solid fa-info"></i></div>
    </div>
  </div>
</template>

<style>
.empty_bd {
  margin: 20px 0px 20px 0;
  border-radius: 5px;
  display: flex;
  flex: 1;
  flex-direction: column;
  height: 100%;
  width: 99%;
  background-color: #FFFFFF;
}

.empty_wrapper {
  position: sticky;
  margin: auto;
  width: 450px;
  height: 150px;
  border-radius: 10px;
  z-index: 2;
  background-color: #DEE6E9;
}

.empty_label {
  text-align: center;
  margin-top: 10px;
  width: 100%;
  color: black;
}

.empty_icon {
  position: sticky;
  color: #DEE6E9;
  background-color: #FFFFFF;
  margin: auto;
  margin-top: 18px;
  width: 80px;
  height: 80px;
  border-radius: 50%;
  font-size: 50px;
}
</style>
