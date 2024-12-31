import LoginPanel from "./components/Login/Login"
import RegisterPannel from "./components/Register/Register"; 
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<RegisterPannel />} />
    </Routes>
  );
}
export default App;
