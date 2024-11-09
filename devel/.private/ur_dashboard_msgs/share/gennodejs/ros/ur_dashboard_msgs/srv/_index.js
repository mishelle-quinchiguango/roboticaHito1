
"use strict";

let IsProgramSaved = require('./IsProgramSaved.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let AddToLog = require('./AddToLog.js')
let Load = require('./Load.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let RawRequest = require('./RawRequest.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let GetRobotMode = require('./GetRobotMode.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let Popup = require('./Popup.js')
let GetProgramState = require('./GetProgramState.js')

module.exports = {
  IsProgramSaved: IsProgramSaved,
  GetLoadedProgram: GetLoadedProgram,
  AddToLog: AddToLog,
  Load: Load,
  IsProgramRunning: IsProgramRunning,
  RawRequest: RawRequest,
  GetSafetyMode: GetSafetyMode,
  GetRobotMode: GetRobotMode,
  IsInRemoteControl: IsInRemoteControl,
  Popup: Popup,
  GetProgramState: GetProgramState,
};
