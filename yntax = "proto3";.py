yntax = "proto3";

package bosdyn.api.spot;

option java_outer_classname = "ChoreographyParamsProto";

import "bosdyn/api/geometry.proto";
import "google/protobuf/wrappers.proto";

// Euler Angle (yaw->pitch->roll) vector.
message EulerZYX {
    double roll = 1;
    double pitch = 2;
    double yaw = 3;
}

// Euler Angle (yaw->pitch->roll) vector that uses wrapped values so we can tell which elements are
// set.
message EulerZYXValue {
    google.protobuf.DoubleValue roll = 1;
    google.protobuf.DoubleValue pitch = 2;
    google.protobuf.DoubleValue yaw = 3;
}