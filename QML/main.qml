import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow
{
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "QML App"

    Item
    {
        id: page
        visible: true
        width: parent.width

        Rectangle
        {
            id: mainRectangle
            height: 160
            width: parent.width
            color: "#eab676"

            Text
            {
                id: mainText
                text: "Regular text"
                height: 30
                width: parent.width
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter

            }

            Button
            {
                id: mainButton
                text: "Ok"
                anchors.top: mainText.bottom
                onClicked: {
                    if (mainRectangle.color == "#abdbe3") {
                        mainRectangle.color = "#eab676"
                    }
                    else {
                            mainRectangle.color = "#abdbe3"
                    }
                }
            }
        }
    }
}