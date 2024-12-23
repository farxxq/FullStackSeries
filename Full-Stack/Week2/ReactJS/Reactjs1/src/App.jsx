import "./App.css";
import React from "react";
import Intro from "./Intro";
import Props from "./Props";
import UseState from "./UseState";
import UseState2 from "./UseState2";

function App() {
  return (
    <>
      <h1 className="mt-4 text-emerald-300 text-4xl text-center font-semibold">
        Assalamwalaikum, Learning the React js!
      </h1>
      <Intro /> {/* Intro component */}
      <div className="mt-10 flex flex-wrap gap-5">
        <Props name="Faroo" bio="Web developer" />{/* Props component */}
        <Props name="Sa" age="22" bio="Researcher" /> {/* Props component */}
        <Props> This is a child props passed</Props> {/* Props component */}
      </div>
      <UseState/> {/* UseState component */}
      <UseState2/>
    </>
  );
}

export default App;
