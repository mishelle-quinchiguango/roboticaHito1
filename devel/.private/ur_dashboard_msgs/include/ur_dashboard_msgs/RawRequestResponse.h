// Generated by gencpp from file ur_dashboard_msgs/RawRequestResponse.msg
// DO NOT EDIT!


#ifndef UR_DASHBOARD_MSGS_MESSAGE_RAWREQUESTRESPONSE_H
#define UR_DASHBOARD_MSGS_MESSAGE_RAWREQUESTRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ur_dashboard_msgs
{
template <class ContainerAllocator>
struct RawRequestResponse_
{
  typedef RawRequestResponse_<ContainerAllocator> Type;

  RawRequestResponse_()
    : answer()  {
    }
  RawRequestResponse_(const ContainerAllocator& _alloc)
    : answer(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _answer_type;
  _answer_type answer;





  typedef boost::shared_ptr< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RawRequestResponse_

typedef ::ur_dashboard_msgs::RawRequestResponse_<std::allocator<void> > RawRequestResponse;

typedef boost::shared_ptr< ::ur_dashboard_msgs::RawRequestResponse > RawRequestResponsePtr;
typedef boost::shared_ptr< ::ur_dashboard_msgs::RawRequestResponse const> RawRequestResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator1> & lhs, const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator2> & rhs)
{
  return lhs.answer == rhs.answer;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator1> & lhs, const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ur_dashboard_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d7e708f879c94bb931716d8f4f130f30";
  }

  static const char* value(const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd7e708f879c94bb9ULL;
  static const uint64_t static_value2 = 0x31716d8f4f130f30ULL;
};

template<class ContainerAllocator>
struct DataType< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ur_dashboard_msgs/RawRequestResponse";
  }

  static const char* value(const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string answer\n"
"\n"
;
  }

  static const char* value(const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.answer);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RawRequestResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ur_dashboard_msgs::RawRequestResponse_<ContainerAllocator>& v)
  {
    s << indent << "answer: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.answer);
  }
};

} // namespace message_operations
} // namespace ros

#endif // UR_DASHBOARD_MSGS_MESSAGE_RAWREQUESTRESPONSE_H
