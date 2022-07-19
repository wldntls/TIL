import { StatusBar } from 'expo-status-bar';
import { useState } from 'react';
import { StyleSheet, Text, View, ScrollView } from 'react-native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

// 메인 화면에 가로로 클릭해서 할지?
// 아니면 스크롤로 내려서 할지?
// 그리고 추가적인 내용필요 없을지?
// 

export default function App() {
  const Tab = createBottomTabNavigator();
  const BottomTabs = () => {
    return (
      <Tab.Navigator>
        <Tab.Screen name="Home" component={Typography_Ex} />
        <Tab.Screen name="상세페이지" component={O_Dictionary} />
        <Tab.Screen name="옵션" component={O_Array} />
      </Tab.Navigator>
    );
  };
  return (
    <View style={styles.container}>
      <StatusBar style="auto" />
      <ScrollView>
        <Text style={styles.header}>오늘의 양조장</Text>
        <ScrollView
          horizontal>
          {/* 사진 추가 어떻게? */}
        </ScrollView>
        <Text>오늘의 술</Text>
        <ScrollView
          horizontal>
          {/* 사진 추가 어떻게? */}
        </ScrollView>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingHorizontal: 20,
    paddingTop: 50,
  },
  header: {
    justifyContent: "space-between",
    flexDirection: "row",
    marginTop: 100,
    fontSize: 40,
    borderRadius: 30
  }
});
