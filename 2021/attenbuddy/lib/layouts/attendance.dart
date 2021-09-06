import 'package:attenbuddyy/components/frame.dart';
import 'package:attenbuddyy/store/store.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class Attendance extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Consumer<Store>(
      builder: (context, store, child) {
        double width = MediaQuery.of(context).size.width;
        double height = MediaQuery.of(context).size.height;

        return Frame(<Widget>[
          Column(
            children: store.listBuilder(context),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                  height: 40,
                  margin: EdgeInsets.fromLTRB(10, 20, 10, 10),
                  child: RaisedButton(
                    onPressed: () async {
                      store.save(context);
                    },
                    shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(80.0)),
                    padding: EdgeInsets.all(0.0),
                    child: Ink(
                      decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: [Colors.green, Colors.greenAccent],
                            begin: Alignment.centerLeft,
                            end: Alignment.centerRight,
                          ),
                          borderRadius: BorderRadius.circular(30.0)),
                      child: Container(
                        constraints: BoxConstraints(
                            maxWidth: width * 0.7, minHeight: 50.0),
                        alignment: Alignment.center,
                        child: Text(
                          "Save",
                          textAlign: TextAlign.center,
                          style: TextStyle(color: Colors.white, fontSize: 15),
                        ),
                      ),
                    ),
                  )),
            ],
          )
        ]);
      },
    );
  }
}
